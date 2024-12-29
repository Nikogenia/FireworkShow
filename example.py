import lib


def scene_1():

    pass

    
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
