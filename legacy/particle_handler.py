# IMPORTS
from particle import PointParticle
import random as rd
from vector.fvector import FVector


# FUNCTIONS

# Rocket launch particle handler
def rocket_launch(particle: PointParticle, delta_time: float) -> None:

    # Update the velocity
    particle.vel = particle.vel.update_y(rd.random() / 20 * delta_time)

    # Update the size
    particle.size -= rd.random() / 5 * delta_time


# Rocket basic explosion particle handler
def rocket_basic_explosion(particle: PointParticle, delta_time: float) -> None:

    # Update the velocity
    particle.vel = particle.vel.update_y(rd.random() / 15 * delta_time)

    # Update the size
    particle.size -= rd.random() / 18 * delta_time


# Rocket image explosion particle handler
def rocket_image_explosion(particle: PointParticle, delta_time: float) -> None:

    # Update the velocity
    particle.vel = particle.vel.update_y(rd.random() / 15 * delta_time)

    # Update the size
    particle.size -= rd.random() / 20 * delta_time
