# IMPORTS
import time as _tm
import datetime as _dt
from constants import WIN_RENDER_SPEED


# FUNCTIONS

# Wait for a time
def wait(duration: float) -> None:
    _tm.sleep(duration)


# Get the absolut time since the epoch
def abs_time() -> float:
    return _tm.time()


# Get the absolut time since the epoch in nanoseconds
def abs_time_ns() -> float:
    return _tm.time_ns()


# Get the run time
def run_time() -> float:
    return _tm.perf_counter()


# Get the run time in nanoseconds
def run_time_ns() -> float:
    return _tm.perf_counter_ns()


# Get formatted time [format 1]
def time_f1() -> str:
    return _dt.datetime.now().strftime("%H:%M:%S")


# Get formatted date [format 1]
def date_f1() -> str:
    return _dt.datetime.now().strftime("%d/%b/%y")


# Get formatted date and time [format 1]
def datetime_f1() -> str:
    return _dt.datetime.now().strftime("%d/%b/%y %H:%M:%S")


# Get formatted date and time [format 2]
def datetime_f2() -> str:
    return _dt.datetime.now().strftime("%Y-%m-%d_%Hh-%Mm-%Ss")


# Get a custom formatted date and time
def datetime_custom(custom_format: str) -> str:
    return _dt.datetime.now().strftime(custom_format)


# CLASSES

# Clock
class Clock:

    # CONSTRUCTOR
    def __init__(self, track_fps: int, update_speed: int = 5) -> None:

        # Define the track information
        from pygame.time import Clock
        self.track_fps: int = track_fps
        self.track_clock: Clock = Clock()

        # Define statistic information
        self.start_time: float = 0
        self.frame_count: int = 0
        self.frame_start: float = 0
        self.frame_end: float = 0
        self.frame_durations: list[float] = [0] * update_speed
        self.frame_duration: float = 1
        self.last_update: float = 0

        # Define delta time information
        self.delta_time: float = 0
        self.last_time: float = 0


    # PROPERTIES

    # FPS
    @property
    def fps(self) -> float:
        return round(self.track_clock.get_fps(), 5)

    # Available FPS
    @property
    def available_fps(self) -> float:
        return round(1 / self.frame_duration, 5)

    # Run time
    @property
    def run_time(self) -> float:
        return round(run_time() - self.start_time, 5)


    # METHODS

    # Tick
    def tick(self, track_fps: int | None = None):

        # Set the frame end
        self.frame_end: float = run_time()

        # Update the frame durations
        self.frame_durations.append(self.frame_end - self.frame_start)
        del self.frame_durations[0]
        if run_time() - self.last_update > 0.3:
            self.frame_duration: float = sum(self.frame_durations) / len(self.frame_durations)
            if self.frame_duration == 0:
                self.frame_duration: float = 1
            self.last_update: float = run_time()

        # Set the track fps
        if track_fps is not None:
            self.track_fps: int = track_fps

        # Wait for the next frame
        self.track_clock.tick(self.track_fps)

        # Update the frame count
        self.frame_count += 1

        # Update the delta time
        self.delta_time: float = run_time() - self.last_time
        self.last_time: float = run_time()
        self.delta_time *= 60 * WIN_RENDER_SPEED

        # Set the frame start
        self.frame_start: float = run_time()
