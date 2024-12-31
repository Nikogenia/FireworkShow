class Animation:

    def __init__(self, width, height, fps, length):

        self.width = width
        self.height = height
        self.fps = fps
        self.length = length

        self.cursor = 0

        self.rockets = {}
        self.fountains = {}

    @property
    def size(self):
        return self.width, self.height

    def wait(self, frames):
        self.cursor += frames

    def jump(self, frame):
        self.cursor = frame

    def spawn_rocket(self, rocket):
        if self.cursor not in self.rockets:
            self.rockets[self.cursor] = []
        self.rockets[self.cursor].append(rocket.copy())

    def explode_rocket(self, rocket):
        if self.cursor - rocket.duration not in self.rockets:
            self.rockets[self.cursor - rocket.duration] = []
        self.rockets[self.cursor - rocket.duration].append(rocket.copy())

    def spawn_fountain(self, fountain):
        if self.cursor not in self.fountains:
            self.fountains[self.cursor] = []
        self.fountains[self.cursor].append(fountain.copy())
