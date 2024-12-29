class Animation:

    def __init__(self, width, height, fps, length):

        self.width = width
        self.height = height
        self.fps = fps
        self.length = length

        self.cursor = 0

        self.rockets = []

    @property
    def size(self):
        return self.width, self.height

    def wait(self, frames):
        self.cursor += frames

    def jump(self, frame):
        self.cursor = frame

