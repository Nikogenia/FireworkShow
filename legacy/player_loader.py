# IMPORTS
import pygame as pg
import multiprocessing as mp
from queue import Empty, Full
from multiprocessing.synchronize import Lock
import tm


# CLASSES

# Loader
class Loader(mp.Process):

    # CONSTRUCTOR
    def __init__(self, lock: Lock, process_id: int, task_queue: mp.Queue, result_queue: mp.Queue, info_queue: mp.Queue, s_width: int, s_height: int) -> None:

        # Initialize the process
        mp.Process.__init__(self, name=f"Loader Process #{process_id}", daemon=True)

        # Set the process ID and lock
        self.lock: Lock = lock
        self.process_id: int = process_id

        # Set the task, result and info queue
        self.task_queue: mp.Queue = task_queue
        self.result_queue: mp.Queue = result_queue
        self.info_queue: mp.Queue = info_queue

        # Set the screen dimension
        self.s_width: int = s_width
        self.s_height: int = s_height


    # METHODS

    # Run
    def run(self) -> None:

        # Print info
        self.print(f"Process '{self.name}' started.")

        # Loader loop
        while True:

            # Wait for a new task from the queue
            task: list[int] = Loader.get_from_queue_no_wait(self.task_queue)

            # Get information
            if self.get_info():
                break

            # If the task is none
            if task is None:

                # Sleep for a short time
                tm.wait(0.05)

                # Try to get a task again
                continue

            start = tm.run_time()

            # Load the task
            result: dict[int, tuple[str, tuple[int, int]]] = self.load_task(task)

            # Put the result to the queue
            self.result_queue.put(result)

            # Print info
            if len(task) > 0:
                self.print(f"Process '{self.name}' done the task {task[0]} - {task[len(task) - 1]} in {tm.run_time() - start:.3f} seconds.")

        # Print info
        self.print(f"Process '{self.name}' finished.")

    # Get from queue with no wait
    @staticmethod
    def get_from_queue_no_wait(queue: mp.Queue):
        try:
            return queue.get_nowait()
        except Empty:
            return None

    # Print
    def print(self, text: str) -> None:
        self.lock.acquire()
        print(text)
        self.lock.release()

    # Load a task
    def load_task(self, task: list[int]) -> dict[int, tuple[str, tuple[int, int]]]:

        # Define a result dictionary
        result: dict[int, tuple[str, tuple[int, int]]] = {}

        # Loop for all frames of the task
        for frame in task:

            # Load the frame
            frame_img: pg.Surface = pg.image.load(f"./render_result_img/frame_{frame}.png")

            # Calculate the new size
            resized_size: tuple[int, int] = int(self.s_height / frame_img.get_height() * frame_img.get_width()), self.s_height

            # Resize the image
            resized_img: pg.Surface = pg.transform.scale(frame_img, resized_size)

            # Add the encoded and resized image with the size to the result dictionary
            result[frame] = pg.image.tostring(resized_img, "RGB"), resized_size

        # Return the result
        return result

    # Get information
    def get_info(self) -> bool:

        # Get information from queue
        info: dict = Loader.get_from_queue_no_wait(self.info_queue)

        # If the info is none, return false
        if info is None:
            return False

        # Check for quit
        if info["quit"]:
            return True

        # Update the screen dimension
        self.s_width: int = info["s_width"]
        self.s_height: int = info["s_height"]

        # Return false
        return False
