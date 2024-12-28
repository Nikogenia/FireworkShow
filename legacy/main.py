# IMPORTS

# General
from constants import *
import threading as th
import sys
import os
import random as rd
import ctypes
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""

# Utils
import tm
from color import *
import font
import draw
from vector.vector import Vector
from vector.fvector import FVector
import img_utils

# Particle
from particle import PointParticle

# Rocket
from rocket import BasicRocket, ImageRocket, Rocket
from image_explosion import ImageExplosion

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
        if os.name == "nt":
            ctypes.windll.user32.SetProcessDPIAware()

        # Render surface
        self.r_height: int = 800
        self.r_width: int = int(self.r_height / self.s_height * self.s_width)
        self.render_surface: pg.Surface = pg.Surface(self.r_dim)
        self.render_mode: int = RENDER_MODE_REALTIME
        self.render_frame: int = 0
        self.render_video: cv.VideoWriter | None = None

        # Initialize pygame
        pg.mixer.pre_init(44100, -16, 2, 512)
        pg.init()
        pg.display.set_caption(f"Particle Simulator (by {AUTHOR}) v{VERSION}")

        # Define the font cache
        self.font_cache: dict[str, pg.font.Font] = {}

        # Define display settings
        self.show_info_line: bool = True

        # Define pause
        self.pause: bool = False

        # Define particle information
        self.point_particles: list[PointParticle] = []
        self.particle_count: int = 0

        # Define rocket information
        self.rockets: list[Rocket] = []
        self.rocket_count: int = 0

        # Load all explosion images
        self.explosion_heart: ImageExplosion = ImageExplosion(pg.image.load("./explosions/Heart.png"), 1.0, 0.5)
        self.explosion_star5: ImageExplosion = ImageExplosion(pg.image.load("./explosions/Star5.png"), 1.0, 0.5)
        self.explosion_luck: ImageExplosion = ImageExplosion(pg.image.load("./explosions/Luck.png"), 1.0, 0.5)
        self.explosion_2024: ImageExplosion = ImageExplosion(pg.image.load("./explosions/2024.png"), 1.2, 0.7)
        self.explosion_images: list[ImageExplosion] = [self.explosion_heart, self.explosion_star5, self.explosion_luck, self.explosion_2024]

        # Load audio
        self.sfx_explosion1: pg.mixer.Sound = pg.mixer.Sound("./sfx/rocket_explosion_1.wav")
        self.sfx_launch1: pg.mixer.Sound = pg.mixer.Sound("./sfx/rocket_launch_1.wav")

    # PROPERTIES

    # Screen dimension
    @property
    def s_dim(self) -> Vector:
        return Vector(self.s_width, self.s_height)

    # Screen center
    @property
    def s_center(self) -> Vector:
        return self.s_dim / 2

    # Render surface dimension
    @property
    def r_dim(self) -> Vector:
        return Vector(self.r_width, self.r_height)

    # Render surface center
    @property
    def r_center(self) -> Vector:
        return self.r_dim / 2


    # METHODS

    # Run
    def run(self) -> None:

        # Setup rendering
        if self.render_mode == RENDER_MODE_RENDER_IMG:

            # Print info
            print("Setup rendering ...")

            # If the render directory already exist, delete it
            if os.path.exists("./render_result_img"):
                for file in os.scandir("./render_result_img"):
                    os.remove(file.path)
                os.rmdir("./render_result_img")

            # Create the directory
            os.mkdir("./render_result_img")

        elif self.render_mode == RENDER_MODE_RENDER_VID:

            # Print info
            print("Setup rendering ...")

            # Open the video writer
            self.render_video: cv.VideoWriter = cv.VideoWriter('./render_result_vid.avi', cv.VideoWriter_fourcc(*'DXVI'), 60, self.s_dim)

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

            # Define the delta time
            delta_time: float = self.clock.delta_time if self.render_mode == RENDER_MODE_REALTIME else 1

            # If the simulation is not paused
            if not self.pause:

                # Spawn new rockets
                if rd.randint(1, 45) == 1:
                    for i in range(rd.randint(1, 3)):
                        if rd.randint(1, 2) == 1:
                            self.rockets.append(BasicRocket(FVector(rd.randint(150, self.r_width - 150), self.r_height + 10), rd.randint(100, 350),
                                                            self.point_particles, self.lock))
                        else:
                            self.rockets.append(ImageRocket(FVector(rd.randint(150, self.r_width - 150), self.r_height + 10), rd.randint(100, 350),
                                                            self.point_particles, self.lock, rd.choice(self.explosion_images)))
                    self.sfx_launch1.play()

                # Handle rockets
                rockets_to_remove: list[Rocket] = []
                for rocket in self.rockets:
                    if rocket.update(delta_time):
                        rockets_to_remove.append(rocket)
                for rocket in rockets_to_remove:
                    self.rockets.remove(rocket)
                    self.sfx_explosion1.play()

                # Handle particles
                particles_to_remove = []
                for particle in self.point_particles:
                    particle.update(delta_time)
                    if particle.size < 1:
                        particles_to_remove.append(particle)
                for particle in particles_to_remove:
                    self.point_particles.remove(particle)

            # Update particle and rocket count
            if self.clock.frame_count % 5 == 0:
                self.particle_count: int = len(self.point_particles)
                self.rocket_count: int = len(self.rockets)

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

        # If the video render mode is activated, release the writer
        if self.render_mode == RENDER_MODE_RENDER_VID:
            self.render_video.release()

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
                if not self.render_mode == RENDER_MODE_RENDER_VID:
                    self.r_width: int = int(self.r_height / self.s_height * self.s_width)
                    self.render_surface: pg.Surface = pg.Surface(self.r_dim)

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
                        if not self.render_mode == RENDER_MODE_RENDER_VID:
                            self.r_width: int = int(self.r_height / self.s_height * self.s_width)
                            self.render_surface: pg.Surface = pg.Surface(self.r_dim)
                    else:
                        pg.display.toggle_fullscreen()
                        self.screen: pg.Surface = pg.display.set_mode((self.non_full_screen_width, self.non_full_screen_height), pg.RESIZABLE)
                        self.s_width: int = self.non_full_screen_width
                        self.s_height: int = self.non_full_screen_height
                        if not self.render_mode == RENDER_MODE_RENDER_VID:
                            self.r_width: int = int(self.r_height / self.s_height * self.s_width)
                            self.render_surface: pg.Surface = pg.Surface(self.r_dim)

                    # Print info
                    print(f"Switched full screen to {str(self.full_screen).lower()}.")

                elif event.key == pg.K_i:

                    # Switch show info line
                    self.show_info_line: bool = not self.show_info_line

                    # Hide or show the mouse
                    pg.mouse.set_visible(self.show_info_line)

                    # Print info
                    print(f"Switched show info line to {str(self.show_info_line).lower()}.")

                elif event.key == pg.K_SPACE:

                    # Switch pause
                    self.pause: bool = not self.pause

                    # Print info
                    print("Simulation paused." if self.pause else "Simulation resumed.")

    # Update the screen
    def update_screen(self) -> None:

        # Fill the screen and render_surface
        draw.rect(self.screen, 0, self.s_height - 40, self.s_width, 40, BLACK)
        self.render_surface.fill(DARK_BLACK)

        # Draw all particles
        for particle in self.point_particles:
            particle.draw(self.render_surface)

        # If the image render mode is activated, save the image
        if self.render_mode == RENDER_MODE_RENDER_IMG:
            pg.image.save(self.render_surface, f"./render_result_img/frame_{self.render_frame}.png")

        # If the video render mode is activated, write to the video
        if self.render_mode == RENDER_MODE_RENDER_VID:
            self.render_video.write(img_utils.pg_to_cv(self.render_surface))

        # Resize the render surface and draw it on the screen
        self.screen.blit(pg.transform.scale(self.render_surface, (self.s_width, self.s_height)), (0, 0))
        # self.screen.blit(img_utils.pg_resize(self.render_surface, self.s_width, self.s_height), (0, 0))

        # Draw the info line
        if self.show_info_line:
            draw.rect(self.screen, 3, self.s_height - 25, self.s_width - 6, 22, BLACK, 100)
            particle_rocket_display_text, text_width, text_height = font.render_text(f"Particles: {self.particle_count}   Rockets: {self.rocket_count}   Display: {self.s_width} x {self.s_height}", font.HP_SIMPLIFIED_18, WHITE)
            self.screen.blit(particle_rocket_display_text, (6, self.s_height - 15 - text_height // 2))
            frame_fps_text, text_width, text_height = font.render_text(f"Frame: {self.render_frame}   FPS: {self.clock.available_fps:.1f} [{self.clock.fps:.1f}]", font.HP_SIMPLIFIED_18, WHITE)
            self.screen.blit(frame_fps_text, (self.s_width - 6 - text_width, self.s_height - 15 - text_height // 2))

        # Update the frame
        if not self.pause:
            self.render_frame += 1

        # Flip the display
        pg.display.flip()


# MAIN
if __name__ == '__main__':

    # Print header
    print("Particle Simulator")
    print("------------------")
    print("")
    print(f"Author: {AUTHOR}")
    print(f"Version: {VERSION}")
    print("")

    # Initialize and start the application
    App().start()
