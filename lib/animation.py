class Animation:

    def __init__(self, width, height, fps, length, offset=0):

        self.width = width
        self.height = height
        self.fps = fps
        self.length = length
        self.offset = offset

        self.cursor = 0

        self.rockets = {}
        self.fountains = {}

    @property
    def size(self):
        return self.width, self.height

    def wait(self, frames):
        self.cursor += frames

    def jump(self, frame, second=0, minute=0):
        self.cursor = int(frame + second * self.fps + minute * self.fps * 60) - self.offset

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
