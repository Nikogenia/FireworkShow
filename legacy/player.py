# IMPORTS

# General
import os
from constants import *
import multiprocessing as mp
from multiprocessing.synchronize import Lock
from queue import Empty, Full
import threading as th
import sys
import random as rd

# Utils
import tm
from color import *
import font
import draw
from vector.vector import Vector
from player_loader import Loader

# Libraries
import pygame as pg


# CLASSES

# Application
class App:

    # CONSTRUCTOR
    def __init__(self) -> None:

        # Print info
        print("Initialize ...")

        # Process lock
        self.lock: Lock = mp.Lock()

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
        self.last_frame: int = 0
        self.frames: dict[int, tuple[str, tuple[int, int]]] = {}

        # Define loader process information
        self.loaders: list[tuple[Loader, mp.Queue]] = []
        self.task_queue: mp.Queue = mp.Queue()
        self.result_queue: mp.Queue = mp.Queue()
        self.package_size: int = 20
        self.loaded_packages: list[int] = []


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

    # Load the last frame
    def load_last_frame(self) -> None:

        # Print info
        print("Load animation ...")

        # Reset the last frame
        self.last_frame: int = 0

        # Load the last frame
        while True:
            if not os.path.exists(f"./render_result_img/frame_{self.last_frame}.png"):
                break
            self.last_frame += 1

    # Start loaders
    def start_loaders(self) -> None:

        # Print info
        print("Start loaders ...")

        # Create loaders
        for process_id in range(8):

            # Create an info queue for the loader
            info_queue: mp.Queue = mp.Queue()

            # Create the loader process
            loader: Loader = Loader(self.lock, process_id, self.task_queue, self.result_queue, info_queue, self.s_width, self.s_height)

            # Save the loader
            self.loaders.append((loader, info_queue))

        # Start loaders
        for loader, info_queue in self.loaders:

            # Start the loader
            loader.start()

    # Send information
    def send_info(self, quit: bool = False) -> None:

        # Define the information
        info: dict = {
            "quit": quit,
            "s_width": self.s_width,
            "s_height": self.s_height
        }

        # Send the information to all loaders
        for loader, info_queue in self.loaders:
            info_queue.put(info)

    # Read frames
    def read_frames(self) -> None:

        # Read frames from queue
        try:
            result: dict[int, tuple[str, tuple[int, int]]] = self.result_queue.get_nowait()
        except Empty:
            return

        # Add all frames to the frame dictionary
        for frame, image in result.items():
            tm.wait(0.05)
            self.frames[frame] = image

    # Manage frames
    def manage_frames(self) -> None:

        # Read frames
        th.Thread(target=self.read_frames, name="Frame reader", daemon=True).start()

        # Delete the previous frame
        if self.frame - 1 in self.frames:
            self.frames.pop(self.frame - 1)

        # Load new frames
        for i in range(10):
            package = self.frame // self.package_size + i
            if package not in self.loaded_packages:
                task = [self.frame + self.package_size * i + frame for frame in range(self.package_size) if self.frame + self.package_size * i + frame < self.last_frame]
                self.task_queue.put(task)
                self.loaded_packages.append(package)

    # Run
    def run(self) -> None:

        # Load the animation
        self.load_last_frame()

        # Start the loaders
        self.start_loaders()

        # Print info
        print("Start ...")

        # Open the window
        self.screen: pg.Surface = pg.display.set_mode(self.s_dim, pg.RESIZABLE)

        # Loop
        while self.running:

            # Wait for the next frame
            self.clock.tick()

            # Handle events
            self.handle_events()

            # Manage frames
            self.manage_frames()

            # Update the screen
            self.update_screen()

        # Close the window
        pg.quit()

        # Quit the application
        self.quit()

    # Quit
    def quit(self) -> None:

        # Print info
        print("Quit ...")

        # Send quit information to all loaders
        self.send_info(True)

        # Kill all processes
        for process in self.loaders:
            process[0].kill()

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
                self.send_info()

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
                        self.send_info()
                    else:
                        pg.display.toggle_fullscreen()
                        self.screen: pg.Surface = pg.display.set_mode((self.non_full_screen_width, self.non_full_screen_height), pg.RESIZABLE)
                        self.s_width: int = self.non_full_screen_width
                        self.s_height: int = self.non_full_screen_height
                        self.send_info()

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
        if self.frame >= self.last_frame - 1:
            self.loaded_packages.clear()
            self.frames.clear()
            self.frame: int = 0

        # If the frame is available
        if self.frame in self.frames:

            # Decode the frame
            frame: pg.Surface = pg.image.fromstring(self.frames[self.frame][0], self.frames[self.frame][1], "RGB")

            # Draw the frame
            self.screen.blit(frame, (self.s_center.x - frame.get_width() // 2, 0))

        # Else
        else:

            # Draw text no image available
            no_img_available_text, text_width, text_height = font.render_text("NO IMAGE AVAILABLE", font.MAIAN_30, WHITE)
            self.screen.blit(no_img_available_text, (self.s_center.x - text_width // 2, self.s_center.y - text_height // 2))

        biggest = 0
        for idx, image in self.frames.copy().items():
            if idx > biggest:
                biggest = idx

        # Draw the info line
        if self.show_info_line:
            draw.rect(self.screen, 3, self.s_height - 25, self.s_width - 6, 22, BLACK, 100)
            frame_text, text_width, text_height = font.render_text(f"Frame: {self.frame}   Loaded: {biggest}   {'Loading' if self.frame == biggest else ''}", font.HP_SIMPLIFIED_18, WHITE)
            self.screen.blit(frame_text, (6, self.s_height - 15 - text_height // 2))
            fps_text, text_width, text_height = font.render_text(f"FPS: {self.clock.available_fps:.1f} [{self.clock.fps:.1f}]", font.HP_SIMPLIFIED_18, WHITE)
            self.screen.blit(fps_text, (self.s_width - 6 - text_width, self.s_height - 15 - text_height // 2))

        # Update the frame
        if not self.pause and self.frame + 1 in self.frames:
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
    App().run()
