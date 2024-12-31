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

    explosion = lib.ImageExplosion(star4_yellow, scale=2.4, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 + 300), lib.FVector(960 - 600, 1100), 90)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.ImageExplosion(star4_yellow, scale=2, strength=0.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 120, 400 + 150), lib.FVector(960 + 100, 1100), 95)
    animation.explode_rocket(rocket)
    animation.wait(50)

    explosion = lib.ImageExplosion(star4_yellow, scale=1.6, strength=0.3)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 440, 400 + 400), lib.FVector(960 + 650, 1100), 100)
    animation.explode_rocket(rocket)
    
    animation.jump(frame=20, second=15)

    fountain = lib.Fountain(lib.FVector(0, 1200), 315, 60, [GREEN, DARK_GREEN, LIME, DARK_LIME], [2, 3, 4], scale=2, strength=3, spread=3)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(1920, 1200), 225, 60, [GREEN, DARK_GREEN, LIME, DARK_LIME], [2, 3, 4], scale=2, strength=3, spread=3)
    animation.spawn_fountain(fountain)


def scene_3():

    animation.jump(frame=42, second=15)

    explosion = [lib.LineExplosion([LIGHT_YELLOW, YELLOW, LIGHT_YELLOW, WHITE], scale=1.5, strength=0.5, lines=18),
                 lib.BasicExplosion([GREEN, DARK_GREEN, LIME, DARK_LIME], scale=1.5, strength=4)]
    rocket = lib.Rocket(explosion, lib.FVector(960 - 100, 400), lib.FVector(960, 1100), 150)
    animation.explode_rocket(rocket)

    animation.jump(frame=50, second=16)

    fountain = lib.Fountain(lib.FVector(960 - 800, 1070), 290, 150, [LIME, DARK_LIME, LIGHT_LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 + 800, 1070), 250, 150, [LIME, DARK_LIME, LIGHT_LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 - 600, 1070), 295, 150, [LIME, DARK_LIME, LIGHT_LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 + 600, 1070), 245, 150, [LIME, DARK_LIME, LIGHT_LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 - 400, 1070), 300, 150, [LIME, DARK_LIME, LIGHT_LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 + 400, 1070), 240, 150, [LIME, DARK_LIME, LIGHT_LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    animation.jump(frame=44, second=18)

    explosion = lib.BasicExplosion([LIME, DARK_LIME, LIGHT_LIME, GREEN], scale=1.5, strength=1.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 700, 400 + 200), lib.FVector(960 - 900, 1100), 120)
    animation.explode_rocket(rocket)
    animation.wait(13)

    rocket = lib.Rocket([explosion], lib.FVector(960 + 650, 400 + 250), lib.FVector(960 + 920, 1100), 130)
    animation.explode_rocket(rocket)
    animation.wait(13)

    rocket = lib.Rocket([explosion], lib.FVector(960 + 120, 400 - 150), lib.FVector(960 + 200, 1100), 110)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = [lib.LineExplosion([LIGHT_YELLOW, YELLOW, LIGHT_YELLOW, WHITE], scale=1.5, strength=0.5, lines=18),
                 lib.BasicExplosion([GREEN, DARK_GREEN, LIME, DARK_LIME], scale=1.5, strength=4)]
    rocket = lib.Rocket(explosion, lib.FVector(960 + 50, 400), lib.FVector(960, 1100), 150)
    animation.explode_rocket(rocket)

    animation.jump(frame=31, second=20)

    explosion = lib.ImageExplosion(luck_green, scale=1.2, strength=0.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 600, 400 - 100), lib.FVector(960 - 800, 1100), 130)
    animation.explode_rocket(rocket)
    animation.wait(25)

    rocket = lib.Rocket([explosion], lib.FVector(960 + 600, 400 - 150), lib.FVector(960 + 800, 1100), 135)
    animation.explode_rocket(rocket)

    animation.jump(frame=58, second=21)
    
    explosion = lib.BasicExplosion([LIGHT_LIME, LIME, DARK_LIME], scale=1.2, strength=4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 100, 400), lib.FVector(960, 1100), 150)
    animation.explode_rocket(rocket)


def scene_4():

    animation.jump(frame=40, second=22)

    explosion = lib.BasicExplosion([ORANGE, DARK_ORANGE], scale=2, strength=4)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 100, 400), lib.FVector(960, 1100), 150)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.BasicExplosion([ORANGE, DARK_ORANGE], scale=2, strength=4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 200, 400 + 200), lib.FVector(960, 1100), 120)
    animation.explode_rocket(rocket)

    animation.jump(frame=56, second=23)

    explosion = lib.ImageExplosion(star5_yellow, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 - 50), lib.FVector(960 - 600, 1100), 130)
    animation.explode_rocket(rocket)
    animation.wait(25)

    rocket = lib.Rocket([explosion], lib.FVector(960, 400 - 150), lib.FVector(960 + 50, 1100), 135)
    animation.explode_rocket(rocket)
    animation.wait(25)

    rocket = lib.Rocket([explosion], lib.FVector(960 + 350, 400 - 100), lib.FVector(960 + 700, 1100), 140)
    animation.explode_rocket(rocket)

    animation.jump(frame=40, second=25)

    fountain = lib.Fountain(lib.FVector(960 - 800, 1070), 290, 150, [ORANGE, DARK_ORANGE, DARK_YELLOW, YELLOW], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 + 800, 1070), 250, 150, [ORANGE, DARK_ORANGE, DARK_YELLOW, YELLOW], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(13)

    fountain = lib.Fountain(lib.FVector(960 - 600, 1070), 295, 150, [ORANGE, DARK_YELLOW, YELLOW], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 + 600, 1070), 245, 150, [ORANGE, DARK_YELLOW, YELLOW], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(13)

    fountain = lib.Fountain(lib.FVector(960 - 400, 1070), 300, 150, [DARK_YELLOW, YELLOW], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 + 400, 1070), 240, 150, [DARK_YELLOW, YELLOW], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    explosion = lib.ImageExplosion(ready_orange, scale=3, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960, 400), lib.FVector(960 - 100, 1100), 130)
    animation.explode_rocket(rocket)

    animation.jump(frame=40, second=29)

    explosion = lib.BasicExplosion([LIGHT_YELLOW, YELLOW], scale=1, strength=1.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 800, 400 + 100), lib.FVector(960 - 100, 1100), 90)
    animation.explode_rocket(rocket)
    animation.wait(15)

    explosion = lib.BasicExplosion([ORANGE, DARK_ORANGE], scale=1, strength=1.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 480, 400 - 40), lib.FVector(960 - 60, 1100), 95)
    animation.explode_rocket(rocket)
    animation.wait(15)

    explosion = lib.BasicExplosion([RED, DARK_RED], scale=1, strength=1.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 150, 400 - 180), lib.FVector(960 - 20, 1100), 100)
    animation.explode_rocket(rocket)
    animation.wait(15)

    explosion = lib.BasicExplosion([PURPLE, DARK_PURPLE], scale=1, strength=1.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 170, 400 - 200), lib.FVector(960 + 20, 1100), 105)
    animation.explode_rocket(rocket)
    animation.wait(15)

    explosion = lib.BasicExplosion([BLUE, DARK_BLUE], scale=1, strength=1.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 500, 400 - 60), lib.FVector(960 + 60, 1100), 110)
    animation.explode_rocket(rocket)
    animation.wait(15)

    explosion = lib.BasicExplosion([GREEN, DARK_GREEN], scale=1, strength=1.4)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 800, 400 + 120), lib.FVector(960 + 100, 1100), 115)
    animation.explode_rocket(rocket)

    fountain = lib.Fountain(lib.FVector(0, 1200), 315, 60, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=2, strength=3, spread=3)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(1920, 1200), 225, 60, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=2, strength=3, spread=3)
    animation.spawn_fountain(fountain)


def scene_5():

    animation.jump(frame=21, second=31)

    explosion = [lib.ImageExplosion(redhair, sizes=[3, 4, 5], scale=2, strength=0.6),
                 lib.LineExplosion([YELLOW, DARK_YELLOW, LIGHT_YELLOW], scale=1.2, strength=0.8)]
    rocket = lib.Rocket(explosion, lib.FVector(960, 400), lib.FVector(980, 1100), 140)
    animation.explode_rocket(rocket)

    explosion = lib.BasicExplosion([YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], scale=2, strength=3)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 500, 400 - 100), lib.FVector(960 - 400, 1100), 120)
    animation.explode_rocket(rocket)

    explosion = lib.BasicExplosion([YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], scale=2, strength=3)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 550, 400 - 120), lib.FVector(960 + 400, 1100), 120)
    animation.explode_rocket(rocket)

    animation.jump(frame=6, second=33)

    explosion = lib.ImageExplosion(y2024_green, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 500, 400 - 100), lib.FVector(960 - 100, 1100), 140)
    animation.explode_rocket(rocket)

    fountain = lib.Fountain(lib.FVector(960 + 100, 1070), 290, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 100, 1070), 250, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 + 300, 1070), 295, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 300, 1070), 245, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 + 500, 1070), 300, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 500, 1070), 240, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 + 700, 1070), 300, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 700, 1070), 240, 150, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    
    animation.jump(frame=49, second=34)

    explosion = lib.ImageExplosion(a_aqua, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 400, 400 - 200), lib.FVector(960 + 100, 1100), 140)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.ImageExplosion(year_aqua, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 100, 400), lib.FVector(960 + 50, 1100), 130)
    animation.explode_rocket(rocket)
    animation.wait(25)

    explosion = lib.ImageExplosion(is_aqua, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 700, 400 + 100), lib.FVector(960 + 150, 1100), 120)
    animation.explode_rocket(rocket)
    animation.wait(50)

    explosion = lib.ImageExplosion(over_blue, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 200, 400 + 300), lib.FVector(960, 1100), 110)
    animation.explode_rocket(rocket)
    
    animation.jump(frame=25, second=37)

    explosion = lib.LineExplosion([LIGHT_BLUE, LIGHT_AQUA, YELLOW, LIGHT_YELLOW, WHITE], lines=15, scale=1.5, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 - 100), lib.FVector(960 + 50, 1100), 120)
    animation.explode_rocket(rocket)

    explosion = lib.LineExplosion([LIGHT_BLUE, LIGHT_AQUA, YELLOW, LIGHT_YELLOW, WHITE], lines=15, scale=1.5, strength=2)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 450, 400 - 150), lib.FVector(960 - 50, 1100), 120)
    animation.explode_rocket(rocket)

    animation.jump(frame=0, second=38)
    fountain = lib.Fountain(lib.FVector(0, 1200), 315, 60, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1.5, strength=2.5, spread=3)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(1920, 1200), 225, 60, [YELLOW, ORANGE, RED, PURPLE, BLUE, AQUA, GREEN, LIME], [2, 3, 4], scale=1.5, strength=2.5, spread=3)
    animation.spawn_fountain(fountain)


def scene_6():

    animation.jump(frame=30, second=38)

    explosion = lib.ImageExplosion(happy_pink, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 - 100), lib.FVector(960 - 100, 1100), 120)
    animation.explode_rocket(rocket)
    
    animation.jump(frame=2, second=40)

    explosion = lib.ImageExplosion(new_red, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 100, 400 + 20), lib.FVector(960 + 100, 1100), 125)
    animation.explode_rocket(rocket)

    fountain = lib.Fountain(lib.FVector(960 + 100, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 100, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 + 300, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 300, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 + 500, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 500, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    animation.wait(25)

    fountain = lib.Fountain(lib.FVector(960 + 700, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)
    fountain = lib.Fountain(lib.FVector(960 - 700, 1070), 270, 150, [RED, DARK_RED, LIGHT_RED], [2, 3, 4], scale=1, strength=1, spread=1)
    animation.spawn_fountain(fountain)

    animation.jump(frame=40, second=41)

    explosion = lib.ImageExplosion(year_red, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 400, 400 - 140), lib.FVector(960 - 100, 1100), 115)
    animation.explode_rocket(rocket)

    animation.jump(frame=15, second=45)

    explosion = lib.ImageExplosion(y2025_gold, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960, 400), lib.FVector(960, 1100), 150)
    animation.explode_rocket(rocket)
    animation.wait(20)

    explosion = lib.ImageExplosion(heart_red, scale=2, strength=0.5)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 600, 400 - 100), lib.FVector(960 - 100, 1100), 140)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 600, 400 - 100), lib.FVector(960 + 100, 1100), 130)
    animation.explode_rocket(rocket)

    explosion = lib.LineExplosion([LIGHT_YELLOW, YELLOW, LIGHT_YELLOW, WHITE], scale=1.5, strength=0.5, lines=12)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 400, 400 - 200), lib.FVector(960 - 600, 1100), 125)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 400, 400 - 200), lib.FVector(960 + 600, 1100), 120)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 - 700, 400 + 200), lib.FVector(960 - 850, 1100), 130)
    animation.explode_rocket(rocket)
    rocket = lib.Rocket([explosion], lib.FVector(960 + 700, 400 + 200), lib.FVector(960 + 850, 1100), 115)
    animation.explode_rocket(rocket)


    
if __name__ == '__main__':

    redhair = pg.image.load("./images/redhair.png")
    welcome_blue = pg.image.load("./images/welcome-blue.png")
    star4_yellow = pg.image.load("./images/star4-yellow.png")
    star5_yellow = pg.image.load("./images/star5-yellow.png")
    heart_red = pg.image.load("./images/heart-red.png")
    luck_green = pg.image.load("./images/luck-green.png")
    ready_orange = pg.image.load("./images/ready-orange.png")
    y2024_green = pg.image.load("./images/2024-green.png")
    y2025_gold = pg.image.load("./images/2025-gold.png")
    a_aqua = pg.image.load("./images/a-aqua.png")
    year_aqua = pg.image.load("./images/year-aqua.png")
    is_aqua = pg.image.load("./images/is-aqua.png")
    over_blue = pg.image.load("./images/over-blue.png")
    happy_pink = pg.image.load("./images/happy-pink.png")
    new_red = pg.image.load("./images/new-red.png")
    year_red = pg.image.load("./images/year-red.png")

    animation = lib.Animation(1920, 1080, 60, 3025, 0)

    scene_1() 
    scene_2()
    scene_3()
    scene_4()
    scene_5()
    scene_6()

    show = lib.Show(animation,
                    name="Firework Show 2025",
                    version="1.0",
                    author="Nikogenia",
                    cache=False,
                    memory_limit=2000,
                    music_path="./music/new-year-bells-short.mp3")

    show.preview()
