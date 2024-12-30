import lib
from lib.color import *


def scene_1():

    explosion = lib.BasicExplosion([RED, ORANGE, YELLOW], scale=2, strength=4)
    rocket = lib.Rocket(explosion, lib.FVector(1200, 400), lib.FVector(1140, 1100), 120)
    animation.spawn_rocket(rocket)

    
if __name__ == '__main__':

    animation = lib.Animation(1920, 1080, 60, 300)

    scene_1()

    show = lib.Show(animation,
                    name="Example",
                    version="1.0",
                    author="Nikogenia",
                    cache=False,
                    memory_limit=2000)

    show.preview()
