import lib
from lib.color import *


def scene_1():

    animation.wait(10)

    explosion = lib.BasicExplosion([RED, ORANGE, YELLOW])
    rocket = lib.Rocket(explosion, lib.FVector(1920/2, 400), lib.FVector(1920/2 - 50, 1100), 50)
    animation.spawn_rocket(rocket)

    
if __name__ == '__main__':

    animation = lib.Animation(1920, 1080, 30, 150)

    scene_1()

    show = lib.Show(animation,
                    name="Example",
                    version="1.0",
                    author="Nikogenia",
                    cache=False,
                    memory_limit=2000)

    show.preview()
