# IMPORTS

# General
import os
from constants import *
import threading as th
import multiprocessing as mp
import sys
import random as rd

# Utils
import tm
from color import *
import font
import draw
from vector.vector import Vector
from vector.fvector import FVector
import img_utils

# Libraries
import pygame as pg
import cv2 as cv


# CLASSES

# Application
class App(th.Thread):

    # CONSTRUCTOR
    def __init__(self) -> None:

        # Initialize the thread
        th.Thread.__init__(self, name="Application Thread")

        # Print info
        print("Initialize ...")

        # Define the threading lock
        self.lock: th.Lock = th.Lock()

        # Define window information
        self.s_width: int = WIN_DEFAULT_WIDTH
        self.s_height: int = WIN_DEFAULT_HEIGHT
        self.screen: pg.Surface = pg.Surface(self.s_dim)
        self.full_screen: bool = False
        self.non_full_screen_width: int = WIN_DEFAULT_WIDTH
        self.non_full_screen_height: int = WIN_DEFAULT_HEIGHT
        self.clock: tm.Clock = tm.Clock(WIN_RENDER_FPS)
        self.running: bool = True

        # Initialize pygame
        pg.init()
        pg.display.set_caption(f"Particle Simulator Video Player (by {AUTHOR}) v{VERSION}")

        # Define the font cache
        self.font_cache: dict[str, pg.font.Font] = {}

        # Define display settings
        self.show_info_line: bool = True

        # Define play information
        self.pause: bool = False
        self.frame: int = 0
        self.frames: list[pg.Surface] = []


    # PROPERTIES

    # Screen dimension
    @property
    def s_dim(self) -> Vector:
        return Vector(self.s_width, self.s_height)

    # Screen center
    @property
    def s_center(self) -> Vector:
        return self.s_dim / 2


    # METHODS

    # Load
    def load(self) -> None:

        # Print info
        print("Load simulation ...")

        # Define frame
        self.frames.clear()
        frame: int = 0
        start: float = tm.run_time()

        # Count frames
        while True:
            if not os.path.exists(f"./render_result_img/frame_{frame}.png"):
                break
            frame += 1

        result_queue = mp.Queue()
        process_count = 4
        chunk_size = frame // process_count
        processes = []
        for i in range(process_count):
            process = mp.Process(target=img_utils.load_images, args=(i, result_queue, [number + i * chunk_size for number in range(chunk_size)], self.s_height), name=f"Loader #{i}", daemon=True)
            processes.append(process)
            process.start()
            print(f"Process {i} started.")
        results = {}
        for i in range(process_count):
            results.update(result_queue.get())
        for process in processes:
            process.join()
        for i in range(chunk_size * process_count):
            self.frames.append(pg.image.fromstring(results[i][0], results[i][1], "RGB"))
            # self.frames.append(img_utils.cv_to_pg(results[i]))

        # thread_count = 8
        # task_size = frame // thread_count
        # tasks = [[number + task * task_size for number in range(task_size)] for task in range(thread_count)]
        #
        # threads = [th.Thread(target=load_images, args=[idx, task], name=f"Loader#{idx}") for idx, task in enumerate(tasks)]
        # thread_results = [None] * len(tasks)
        # for thread in threads:
        #     thread.start()
        # for thread in threads:
        #     thread.join()
        # for result in thread_results:
        #     self.frames.extend(result)

        # # Load loop
        # while True:
        #
        #     # If the next frame doesn't exist, done
        #     if not os.path.exists(f"./render_result_img/frame_{frame}.png"):
        #         break
        #
        #     # Read the frame
        #     img = pg.image.load(f"./render_result_img/frame_{frame}.png")
        #
        #     # Resize the frame and append it to the list
        #     self.frames.append(img_utils.pg_resize(img, int(self.s_height / img.get_height() * img.get_width()), self.s_height))
        #
        #     # Update the frame
        #     frame += 1

        # Print info
        print(f"Loading done in {tm.run_time() - start:.3f} seconds.")

    # Run
    def run(self) -> None:

        # Print info
        print("Start ...")

        # Open the window
        self.screen: pg.Surface = pg.display.set_mode(self.s_dim, pg.RESIZABLE)

        self.load()

        # Loop
        while self.running:

            # Wait for the next frame
            self.clock.tick()

            # Handle events
            self.handle_events()

            # Update the screen
            self.update_screen()

        # Close the window
        # pg.quit()

        # Quit the application
        self.quit()

    # Quit
    def quit(self) -> None:

        # Print info
        print("Quit ...")

        # Exit the program
        sys.exit(0)

    # Handle events
    def handle_events(self) -> None:

        # Loop for all events
        for event in pg.event.get():

            # Check for window events
            if event.type == pg.QUIT:

                # Set running to false
                self.running: bool = False

            elif event.type == pg.WINDOWRESIZED:

                # Update the screen size
                self.s_width: int = WIN_MIN_WIDTH if event.x < WIN_MIN_WIDTH else event.x
                self.s_height: int = WIN_MIN_HEIGHT if event.y < WIN_MIN_HEIGHT else event.y
                if not self.full_screen:
                    self.screen: pg.Surface = pg.display.set_mode(self.s_dim, pg.RESIZABLE)
                self.load()

                # Print info
                print(f"Resized window to {self.s_width} x {self.s_height}.")

            # Check for key events
            if event.type == pg.KEYDOWN:

                # Check for different keys
                if event.key == pg.K_ESCAPE:

                    # Set running to false
                    self.running: bool = False

                elif event.key == pg.K_f:

                    # Switch full screen
                    self.full_screen: bool = not self.full_screen
                    if self.full_screen:
                        self.non_full_screen_width: int = self.s_width
                        self.non_full_screen_height: int = self.s_height
                        self.screen: pg.Surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
                        self.s_width: int = self.screen.get_width()
                        self.s_height: int = self.screen.get_height()
                        self.load()
                    else:
                        pg.display.toggle_fullscreen()
                        self.screen: pg.Surface = pg.display.set_mode((self.non_full_screen_width, self.non_full_screen_height), pg.RESIZABLE)
                        self.s_width: int = self.non_full_screen_width
                        self.s_height: int = self.non_full_screen_height
                        self.load()

                    # Print info
                    print(f"Switched full screen to {str(self.full_screen).lower()}.")

                elif event.key == pg.K_i:

                    # Switch show info line
                    self.show_info_line: bool = not self.show_info_line

                    # Print info
                    print(f"Switched show info line to {str(self.show_info_line).lower()}.")

                elif event.key == pg.K_SPACE:

                    # Switch pause
                    self.pause: bool = not self.pause

                    # Print info
                    print("Simulation paused." if self.pause else "Simulation resumed.")

    # Update the screen
    def update_screen(self) -> None:

        # Fill the screen
        self.screen.fill(BLACK)

        # Reset the frame, if the animation reached the end
        if self.frame == len(self.frames):
            self.frame: int = 0

        # Draw the frame
        self.screen.blit(self.frames[self.frame], (self.s_center.x - self.frames[self.frame].get_width() // 2, 0))

        # # If the next frame exist
        # if os.path.exists(f"./render_result_img/frame_{self.frame}.png"):
        #
        #     # Read the frame
        #     frame = pg.image.load(f"./render_result_img/frame_{self.frame}.png").convert()
        #
        #     # Resize the frame
        #     resized_frame = pg.transform.scale(frame, (int(self.s_height / frame.get_height() * frame.get_width()), self.s_height))
        #
        #     # Draw the frame
        #     self.screen.blit(resized_frame, (self.s_center.x - resized_frame.get_width() // 2, 0))
        #
        # # Else, set the frame to 0
        # else:
        #     self.frame: int = 0

        # Draw the info line
        if self.show_info_line:
            draw.rect(self.screen, 3, self.s_height - 25, self.s_width - 6, 22, BLACK, 100)
            frame_text, text_width, text_height = font.render_text(f"Frame: {self.frame}", font.HP_SIMPLIFIED_18, WHITE)
            self.screen.blit(frame_text, (6, self.s_height - 15 - text_height // 2))
            fps_text, text_width, text_height = font.render_text(f"FPS: {self.clock.available_fps:.1f} [{self.clock.fps:.1f}]", font.HP_SIMPLIFIED_18, WHITE)
            self.screen.blit(fps_text, (self.s_width - 6 - text_width, self.s_height - 15 - text_height // 2))

        # Update the frame
        if not self.pause:
            self.frame += 1

        # Flip the display
        pg.display.flip()


# MAIN
if __name__ == '__main__':

    # Print header
    print("Particle Simulator Video Player")
    print("-------------------------------")
    print("")
    print(f"Author: {AUTHOR}")
    print(f"Version: {VERSION}")
    print("")

    # Initialize and start the application
    App().start()
