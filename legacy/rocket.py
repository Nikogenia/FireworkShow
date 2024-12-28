# IMPORTS
from vector.fvector import FVector
from color import *
from particle import PointParticle
import random as rd
import particle_handler
import threading as th
from image_explosion import ImageExplosion
from abc import ABCMeta, abstractmethod
import tm


# CONSTANTS

# Rocket launch colors
ROCKET_LAUNCH_COLORS = [WHITE, LIGHT_YELLOW, YELLOW, DARK_YELLOW, ORANGE]

# Rocket basic explosion colors
ROCKET_BASIC_EXPLOSION_COLORS = [YELLOW, RED, LIGHT_BLUE, LIGHT_PURPLE, DARK_LIME]


# CLASSES

# Rocket type
class Rocket(metaclass=ABCMeta):

    # ABSTRACT METHODS

    # Explode
    @abstractmethod
    def explode(self) -> None:
        pass

    # Update
    @abstractmethod
    def update(self, delta_time: float) -> bool:
        pass


# Basic Rocket
class BasicRocket(Rocket):

    # CONSTRUCTOR
    def __init__(self, pos: FVector, height: int, particles: list[PointParticle], lock: th.Lock) -> None:

        # Define rocket information
        self.pos: FVector = pos
        self.height: int = height
        self.x_vel: float = 0

        # Set the particle list and lock
        self.particles: list[PointParticle] = particles
        self.lock: th.Lock = lock


    # METHODS

    # Explode
    def explode(self) -> None:

        # Define explosion particle list
        explosion_particles: list[PointParticle] = []

        # Create the explosion particles
        colors = []
        for i in range(rd.choice([1, 1, 1, 2, 2, 3, 4, 5, 6, 7])):
            colors.append(rd.choice(ROCKET_BASIC_EXPLOSION_COLORS))
        for i in range(rd.randint(250, 400)):
            explosion_particles.append(PointParticle(self.pos, FVector(rd.gauss(0, 1.2), rd.gauss(0, 1.2)), rd.randint(4, 6),
                                                     rd.choice(colors), particle_handler.rocket_basic_explosion, True))

        # Append all explosion particles to the particle list
        self.lock.acquire()
        self.particles.extend(explosion_particles)
        self.lock.release()

    # Update
    def update(self, delta_time: float) -> bool:

        # Check for explosion
        if self.pos.y <= self.height:

            # Explode
            th.Thread(target=self.explode, name="Explosion Thread").start()

            # Return true
            return True

        # Move
        self.x_vel += (rd.random() - 0.5) / 2 * delta_time
        self.pos += self.x_vel, -rd.randint(8, 15) * delta_time * (self.pos.y - self.height + 50) / 400

        # Create launch particles
        for i in range(int(rd.random() * delta_time + (self.pos.y - self.height + 10) / 100)):
            self.particles.append(PointParticle(self.pos, FVector(rd.random() * 1.5 - 0.75, rd.randint(2, 3)), rd.randint(2, 3), rd.choice(ROCKET_LAUNCH_COLORS), particle_handler.rocket_launch))

        # Return false
        return False


    # OVERRIDE METHODS

    # String
    def __str__(self) -> str:
        return f"BasicRocket[pos={self.pos}|height={self.height}|x_vel={self.x_vel}|ID={id(self)}]"


# Image Rocket
class ImageRocket(Rocket):

    # CONSTRUCTOR
    def __init__(self, pos: FVector, height: int, particles: list[PointParticle], lock: th.Lock, explosion: ImageExplosion) -> None:

        # Define rocket information
        self.pos: FVector = pos
        self.height: int = height
        self.x_vel: float = 0

        # Set the particle list and lock
        self.particles: list[PointParticle] = particles
        self.lock: th.Lock = lock

        # Set the image
        self.explosion: ImageExplosion = explosion


    # METHODS

    # Explode
    def explode(self) -> None:

        # Generate all particles from image
        explosion_particles: list[PointParticle] = self.explosion.generate_particles(self.pos)

        # Append all explosion particles to the particle list
        self.lock.acquire()
        self.particles.extend(explosion_particles)
        self.lock.release()

    # Update
    def update(self, delta_time: float) -> bool:

        # Check for explosion
        if self.pos.y <= self.height:

            # Explode
            th.Thread(target=self.explode, name="Explosion Thread").start()

            # Return true
            return True

        # Move
        self.x_vel += (rd.random() - 0.5) / 2 * delta_time
        self.pos += self.x_vel, -rd.randint(8, 15) * delta_time * (self.pos.y - self.height + 10) / 400

        # Create launch particles
        for i in range(int(rd.random() * delta_time + (self.pos.y - self.height + 10) / 100)):
            self.particles.append(PointParticle(self.pos, FVector(rd.random() * 1.5 - 0.75, rd.randint(2, 3)), rd.randint(2, 3), rd.choice(ROCKET_LAUNCH_COLORS), particle_handler.rocket_launch))

        # Return false
        return False

    # OVERRIDE METHODS

    # String
    def __str__(self) -> str:
        return f"ImageRocket[pos={self.pos}|height={self.height}|x_vel={self.x_vel}|ID={id(self)}]"
